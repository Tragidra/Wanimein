// 导入axios实例
import httpRequest from '../request/index'

// 注册
export function register(data) {
	return httpRequest({
		url: '/auth',
		method: 'put',
		data: data,
	})
}

// 登录
export default function login(data) {
    return httpRequest({
		url: '/auth',
		method: 'post',
		data: data,
	})
}

// 获取用户信息
export function getUserInfo(params) {
	return httpRequest({
		url: '/auth',
		method: 'get',
		params: params
	})
}