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
        formElems = document.forms['zkrpack'].elements;
    
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        console.log(formElems);
    });
}

export {addZrString, closePackInfo, newPack};