import { postData } from "../services/requests.js";

const writeZkrPack = (url) => {
    const form = document.forms['zkrpack'].elements;
    let data = {};
    for (let elem of form) {
        if (elem.tagName !== 'BUTTON') {
            data[elem.id] = elem.value;
        }
    }
    postData(url, JSON.stringify(data))
};

export {writeZkrPack};