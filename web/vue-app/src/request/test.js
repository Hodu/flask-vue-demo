import {request} from "../common/request";
export function getMsg() {
  return request({
    url:'/msg',
    method:"get",
  })
}