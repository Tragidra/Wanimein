// 导入axios实例
import httpRequest from '../request/index'


// 获取mov信息
export default function apiGetMovList(param) {
    return httpRequest({
		url: '/movie_info',
		method: 'get',
		params: param,
	})
}

export function apiGetYears(param) {
	return httpRequest({
		url: '/year',
		method: 'get',
		params: param,
	})
}

export function apiGetCountry(param) {
	return httpRequest({
		url: '/country',
		method: 'get',
		params: param,
	})
}

export function apiGetGenres(param) {
	return httpRequest({
		url: '/genre',
		method: 'get',
		params: param,
	})
}