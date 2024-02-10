// 导入axios实例
import httpRequest from '../request/index'

// 注册
export function postComments(data) {
    var url = '/comment'
	return httpRequest({
		url: url,
		method: 'put',
		data: data,
	})
}

export function showComments(param) {
    var url = '/comment'
	return httpRequest({
		url: url,
		method: 'get',
		params: param,
	})
}

export function replyComment(data) {
    var url = '/comment'
	return httpRequest({
		url: url,
		method: 'put',
        data: data
	})
}