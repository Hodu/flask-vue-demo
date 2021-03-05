import { request } from "../common/request";

export function getUsers() {
    return request({
        url:'/user',
        method:"get",
    })
}
