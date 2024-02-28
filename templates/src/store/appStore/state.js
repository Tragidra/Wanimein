function haveToken() {
    const value = window.localStorage.getItem('tokenwanimein')
    if (value) {
        return true
    } else {
        return false
    }
}


export default {
    countVuex: 0,
    type_names: {
        0: [],
        1: [],
        2: [],
        3: []
    },
    isLogining: haveToken(),
    user: {}
}