// 导入axios实例
import httpRequest from '../request/index'


// 获取视频收藏信息
export  function showCollectVideo(param) {
    return httpRequest({
		url: '/collection',
		method: 'get',
		params: param,
	})
}


// 添加视频收藏
export  function addCollectVideo(data) {
    return httpRequest({
		url: '/collection',
		method: 'put',
		data: data,
	})
}

// 删除视频收藏
export  function removeCollectVideo(data) {
    return httpRequest({
		url: '/collection',
		method: 'post',
		data: data,
	})
}


// 该视频是否已被收藏
export function isCollectVideo(param) {
    return httpRequest({
		url: '/check',
		method: 'get',
		params: param,
	})
}