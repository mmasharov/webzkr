import { getResource } from "../services/requests.js";

function fillDropdown(parent, data) {
    for (let item in data) {
        const menuItem = document.createElement('option');
        menuItem.setAttribute('value', item);
        menuItem.textContent = `${item} - ${data[item]}`;
        parent.appendChild(menuItem);
    }
}

const ddList = (id) => {
    const parentElem = document.querySelector(id);
    const name = id.split('-')[1];
    getResource(`http://localhost:8000/${name}/`)
        .then(res => JSON.parse(res))
        .then(json => fillDropdown(parentElem, json));
};

export {ddList};