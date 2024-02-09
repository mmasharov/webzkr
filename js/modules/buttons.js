import { state } from "../main.js";

function trimDropdown(str) {
    return str.split('-')[0].trim();
}

function addZrString() {
    const btn = document.querySelector('#zrst-add_str');
    const elems = document.querySelectorAll("[id^='zrst-']");
    let data = {};
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        elems.forEach(elem => {
            if (elem !== btn) {
                if (elem.tagName === 'SELECT') {
                    data[elem.id] = trimDropdown(elem.value);
                } else {
                    data[elem.id] = elem.value;
                }
            }
        });
        console.log(data);
    });
}

function closePackInfo(callback) {
    const btn = document.querySelector('#closepack'),
        block = document.querySelector('#zkrpack'),
        add = document.querySelector('#addpack');

    btn.addEventListener('click', (e) => {
        e.preventDefault();
        state['packNum'] = 0;
        add.style.display = 'none';
        block.style.display = 'none';
        callback();
    });
}

function newPack() {
    const btn = document.querySelector('#newpack'),
        block = document.querySelector('#zkrpack'),
        add = document.querySelector('#addpack'),
        upd = document.querySelector('#updpack'),
        form = document.forms['zkrpack'];
    
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        state['packNum'] = 0;
        block.style.display = 'block';
        upd.style.display = 'none';
        add.style.display = 'inline';
        for (let elem of form) {
            switch(elem.id) {
                case 'from-budg_level':
                    elem.value = 1;
                    break;
                case 'secure-level':
                    elem.value = 0;
                    break;
                default:
                    elem.value = '';
                    break;
            }
        }
    });
}

function updatePack() {
    const btn = document.querySelector('#updpack');

    btn.addEventListener('click', (e) => {
        e.preventDefault();
        console.log(parseInt(state['packNum']));
    });
}

export {addZrString, closePackInfo, newPack, updatePack};