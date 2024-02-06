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

export {addZrString};