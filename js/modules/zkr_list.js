import { getResource } from "../services/requests.js";

function fillZkrList(parent, data, mod) {
    const parentElem = document.querySelector(parent);
    parentElem.querySelectorAll('.zkr__list_item').forEach((item, i) => {
        if (i !== 0) {
            item.remove();
        }
    });
    for (let item of data) {
        let zkrItem = document.createElement('div');
        zkrItem.classList.add('zkr__list_item');
        if (mod) {
            zkrItem.classList.add(`zkr__list_item-${mod}`);
        }

        for (let cell in item) {
            let cellBlock = document.createElement('div');
            cellBlock.setAttribute('id', cell);
            cellBlock.textContent = item[cell];
            zkrItem.appendChild(cellBlock);
        }

        parentElem.appendChild(zkrItem);
    }
}

function fillZkrInfo(data) {
    for (let item in data) {
        document.querySelector(`#${item}`).value = data[item];
    }
}

const zkrPackList = async (id) => {
    await getResource('http://localhost:8000/zkr_pack/')
        .then(res => fillZkrList(id, res, 'pack'));
};

const zkrList = async (id, parent_id, callback) => {
    await getResource(`http://localhost:8000/zkr/${parent_id}`)
        .then(res => fillZkrList(id, res, 'zr'));
    callback();
};

const zkrStrList = async (id, parent_id) => {
    await getResource(`http://localhost:8000/zrst/${parent_id}`)
        .then(res => fillZkrList(id, res, 'str'));
}

const fillZkrPack = async (id) => {
    await getResource(`http://localhost:8000/zkr_pack/${id}`)
        .then(res => fillZkrInfo(res));
}

export { zkrPackList, zkrList, zkrStrList, fillZkrPack };