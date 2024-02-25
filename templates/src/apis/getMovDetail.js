// 导入axios实例
import httpRequest from '../request/index'


// 获取mov详细信息
export default function apiGetMovDetail(param) {
    return httpRequest({
		url: '/movie_details',
		method: 'get',
		params: param,
	})
}

export function apiGetMovGenres(param){
	return httpRequest({
		url: '/movie_genr',
		method: 'get',
		params: param,
	})
}

export function apiGetMovActors(param){
	return httpRequest({
		url: '/movie_actor',
		method: 'get',
		params: param,
	})
}

export function apiGetMovTags(param){
	return httpRequest({
		url: '/movie_tags',
		method: 'get',
		params: param,
	})
}