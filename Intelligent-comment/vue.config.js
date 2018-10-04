// // vue.config.js
// const path = require('path');
// function resolve (dir) {
//     return path.join(__dirname, dir)
// }
// module.exports = {
//     chainWebpack: config => {
//         //路径配置
//     },
//
//     // webpack-dev-server 相关配置
//     devServer: {
//         // 调试端口
//         // port: 8989
//     },
//     //其他配置....
//     moudle: {
//         rules: [
//             {
//                 test: /\.less/,
//                 use: ExtractTextPlugin.extract({
//                     use: ['css-loader?minimize', 'autoprefixer-loader', 'less-loader'],
//                     fallback: 'style-loader'
//                 })
//             }
//         ]
//     }
// }