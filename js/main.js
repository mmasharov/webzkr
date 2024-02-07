import { ddList } from "./modules/dropdowns.js";
import { addZrString } from "./modules/buttons.js";
import { zkrPackList, zkrList, zkrStrList, fillZkrPack } from "./modules/zkr_list.js";

const dropdowns = ['from-budg_level', 'secure-level', 'zr-type', 'zr-type_ap', 'zr-vid_pl', 'zr-kod_income',
            'zrosn-osn_plat', 'zrst-kod_ist_kbk', 'zrst-type_kbk_pay', 'zrst-type_kbk_rcp'];

let packNum = 0;
let zrNum = 0;

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
                packNum = elem.childNodes[2].textContent;
                zkrList('#zkrlist', packNum, zrListEvent);
                // Очистка списка строк при смене пакета
                document.querySelector('#zkrstrlist').querySelectorAll('.zkr__list_item').forEach((item, i) => {
                    if (i !== 0) {
                        item.remove();
                    }
                });
                if (packNum) {
                    fillZkrPack(packNum);
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
                zrNum = str.childNodes[0].textContent;
                zkrStrList('#zkrstrlist', zrNum);
            });
        }
    });
};

window.addEventListener('DOMContentLoaded', () => {
    // Заполняем выпадающие списки
    for (let dd of dropdowns) {
        ddList(`#${dd}`);
    }
    // TODO строки ЗКР
    addZrString();
    // Заполнение списка пакетов заявок
    renderZkrPackList('#zkrpacklist', packListEvent);

    let test = document.forms['zkrpack'].elements['from-budg_level'].value;
    console.log(test);
    document.querySelector('#from-budg_level').addEventListener('change', () => {
        test = document.forms['zkrpack'].elements['from-budg_level'].value;
        console.log(test);
    })
});