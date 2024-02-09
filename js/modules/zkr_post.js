import { postData } from "../services/requests.js";
import { state } from "../main.js";

const writeZkrPack = (url) => {
    const form = document.forms['zkrpack'].elements;
    let data = {};
    for (let elem of form) {
        if (elem.tagName !== 'BUTTON') {
            data[elem.id] = elem.value;
        }
    }
    data['pack_id'] = state['packNum'];
    postData(url, JSON.stringify(data))
};

export {writeZkrPack};