import { ddList } from "./modules/dropdowns.js";
import { addZrString, closePackInfo, newPack, updatePack } from "./modules/buttons.js";
import { zkrPackList, zkrList, zkrStrList, fillZkrPack, fillZkrInfo } from "./modules/zkr_list.js";
import { writeZkrPack } from "./modules/zkr_post.js";

const dropdowns = ['from-budg_level', 'secure-level', 'zr-type', 'zr-type_ap', 'zr-vid_pl', 'zr-kod_income',
            'zrosn-osn_plat', 'zrst-kod_ist_kbk', 'zrst-type_kbk_pay', 'zrst-type_kbk_rcp'],
            packblock = document.querySelector('#zkrpack'),
            zkrblock = document.querySelector('#zkritem'),
            strblock = document.querySelector('#zkrstr');

let state = {
    packNum: 0,
    zrNum: 0,
    strNum: 0
};

const renderZkrPackList = async (id, callback) => {
    await zkrPackList(id);
    callback(id);
};

const packListEvent = (parentId) => {
    // Назначение обработчиков событий для выбора списка заявок в пакете
    const elems = document.querySelector(parentId).querySelectorAll('.zkr__list_item');
    elems.forEach((elem, i) => {
        if (i !== 0) {
            elem.addEventListener('click', () => {
                state['packNum'] = parseInt(elem.childNodes[2].textContent);
                packblock.style.display = 'block';
                document.querySelector('#updpack').style.display = 'inline';
                zkrList('#zkrlist', state['packNum'], zrListEvent); // Заполняем список заявок в пакете
                // Очистка списка строк при смене пакета
                document.querySelector('#zkrstrlist').querySelectorAll('.zkr__list_item').forEach((item, i) => {
                    if (i !== 0) {
                        item.remove();
                    }
                });
                if (state['packNum']) {
                    fillZkrPack(state['packNum']);
                }
            });
        }
    });
};

const zrListEvent = () => {
    const strings = document.querySelector('#zkrlist').querySelectorAll('.zkr__list_item');
    strings.forEach((str, j) => {
        if (j !== 0) {
            str.addEventListener('click', () => {
                state['zrNum'] = parseInt(str.childNodes[0].textContent);
                zkrblock.style.display = 'block';
                zkrStrList('#zkrstrlist', state['zrNum']); // Заполняем список строк заявки
                if (state['zrNum']) {
                    fillZkrInfo(state['zrNum']);
                }
            });
        }
    });
};

window.addEventListener('DOMContentLoaded', () => {
    if (!state['packNum']) {
        packblock.style.display = 'none';
    }
    if (!state['zrNum']) {
        zkrblock.style.display = 'none';
    }
    if (!state['strNum']) {
        strblock.style.display = 'none';
    }
    // Заполняем выпадающие списки
    for (let dd of dropdowns) {
        ddList(`#${dd}`);
    }
    // TODO строки ЗКР
    addZrString();
    // Заполнение списка пакетов заявок
    renderZkrPackList('#zkrpacklist', packListEvent);

    // Запись в БД нового пакета заявок
    document.querySelector('#addpack').addEventListener('click', (e) => {
        e.preventDefault();
        writeZkrPack('http://localhost:8000/zkr_pack');
    });
    document.querySelector('#updpack').addEventListener('click', (e) => {
        e.preventDefault();
        writeZkrPack('http://localhost:8000/zkr_pack');
    });

    closePackInfo(() => state['packNum'] = 0);
    newPack();
    updatePack();
});

export {state};