
//创建a标签下载
import json2csv from "json2csv";

export function createDownLoadClick(content, fileName) {
  console.log("=====createDownLoadClick")
  const link = document.createElement("a");
  link.href = encodeURI(content);
  link.download = fileName;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
    // 判断是否IE浏览器
export function MyBrowserIsIE(){
  console.log("=====MyBrowserIsIE")
  let isIE = false;
  if (
    navigator.userAgent.indexOf("compatible") > -1 &&
    navigator.userAgent.indexOf("MSIE") > -1
  ) {
    // ie浏览器
    isIE = true;
  }
  if (navigator.userAgent.indexOf("Trident") > -1) {
    // edge 浏览器
    isIE = true;
  }
  return isIE;
}

export function exportCSV(rows, fields, name) {
    try {
      console.log("=====exportCSV")
      name = name && name.indexOf("csv") === -1 ? name + ".csv" : name;
      const result = json2csv.parse(rows, {
        fields: fields,
        excelStrings: true
      });
      console.log("--------s123")
      if (MyBrowserIsIE()) {
        // IE10以及Edge浏览器
        var BOM = "\uFEFF";
                // 文件转Blob格式
        var csvData = new Blob([BOM + result], { type: "text/csv" });
        navigator.msSaveBlob(csvData, `a.csv`);
      } else {
        let csvContent = "data:text/csv;charset=utf-8,\uFEFF" + result;
        // 非ie 浏览器
        createDownLoadClick(csvContent, name);
      }
    } catch (err) {
      alert(err);
    }
}

export default {
  MyBrowserIsIE,
  createDownLoadClick,
  exportCSV,
};
