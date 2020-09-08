import pandas as pd
from django.conf import settings
from sqlalchemy import create_engine

class FoodQuery:

    def __init__(self):
        self.engine = create_engine(settings.HOSTED_DB_URL)

    def check_food(self, food_name):
        cmd='SELECT product_name FROM keto WHERE product_name ilike \'%'+food_name+'%\''
        c=pd.read_sql_query(cmd,con=self.engine)
        if(c.empty):
            return False, ''
        else:
            return True, list(c['product_name'])[0]

    def get_food_list(self, food_name):
        cmd='SELECT DISTINCT product_name FROM keto WHERE product_name ilike \'%'+food_name+'%\''
        c=pd.read_sql_query(cmd,con=self.engine)
        food_list=list(c['product_name'])
        return food_list

    def get_product_details(self, food_name):
        l = self.get_food_list(food_name)
        if(len(l)==0):
            ans="No match"
            return ans
        else:
            item=l[0]
            cmd = 'SELECT energy_100g, fat_100g,carbohydrates_100g, sugars_100g, proteins_100g FROM keto WHERE LOWER(product_name) = \''+item.lower()+'\''
            c=pd.read_sql_query(cmd,con=self.engine)
            ans=food_name + " contains calories of "+str(c['energy_100g'][0])+" grams,"+" carbs of "+str(c['carbohydrates_100g'][0])+" grams, "+"sugars of "+str(c['sugars_100g'][0])+" grams and proteins of "+str(c['proteins_100g'][0])+" grams"

            return ans


def get_answer(intent, food):
    fq = FoodQuery()

    if(intent == "check_keto"):
        db_quer_res, f = fq.check_food(food)

        if(db_quer_res == True):
            return 'Yes, you can have '+str(food)+' in your Keto diet. Check out '+str(f)+'. It is made for Keto.'
        else:
            return 'According to my database, you cannot have '+str(food)+' in your Keto diet'

    elif(intent == "food_suggestion"):
        food_lst = fq.get_food_list(food)

        if(len(food_lst) == 0):
            return 'Sorry, I did not find any match for '+str(food)
        else:
            resp_str = 'You can check out'
            i = 0
            for f in food_lst:
                resp_str += ' '+str(f)+','
                i += 1

                if(i >= 4):
                    break

            return resp_str[:-1]

    elif(intent == "food_details"):
        detials = fq.get_product_details(food)

        if(detials == "No match"):
            return 'Sorry, I did not find any match for ' + str(food)
        else:
            return detials