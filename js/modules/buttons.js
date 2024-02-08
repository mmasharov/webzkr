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
        block = document.querySelector('#zkrpack');

    btn.addEventListener('click', (e) => {
        e.preventDefault();
        block.style.display = 'none';
        callback();
    });
}

function newPack(packNum) {
    const btn = document.querySelector('#newpack'),
        block = document.querySelector('#zkrpack'),
        formElems = document.forms['zkrpack'];
    
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        block.style.display = 'block';
        for (let elem of formElems) {
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

export {addZrString, closePackInfo, newPack};