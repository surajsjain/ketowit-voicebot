'use strict';

// const socket = io();

const outputYou = document.querySelector('.output-you');
const outputBot = document.querySelector('.output-bot');

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

document.querySelector('button').addEventListener('click', () => {
    recognition.start();
});

recognition.addEventListener('speechstart', () => {
    // console.log('Speech has been detected.');
});

recognition.addEventListener('result', (e) => {
    // console.log('Result has been detected.');

    let last = e.results.length - 1;
    let text = e.results[last][0].transcript;

    outputYou.textContent = text;
    // console.log('Confidence: ' + e.results[0][0].confidence);

    // outputBot.textContent = "I know that you said "+text;
    // synthVoice("I know that you said "+text);

    // socket.emit('chat message', text);

    outputBot.textContent = "...";

    var xhr = new XMLHttpRequest();
    var url = "bot/";

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var resp = xhr.responseText;
            var resp_obj = JSON.parse(resp);
            outputBot.textContent = resp_obj['ans'];
            synthVoice(resp_obj['ans']);
            // console.log(resp_obj);
        }
    };

    var data = {
        "utterance": text
    }

    xhr.send(JSON.stringify(data));
});

recognition.addEventListener('speechend', () => {
    recognition.stop();
});

recognition.addEventListener('error', (e) => {
    outputBot.textContent = 'Error: ' + e.error;
});

function synthVoice(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance();
    utterance.text = text;
    synth.speak(utterance);
}