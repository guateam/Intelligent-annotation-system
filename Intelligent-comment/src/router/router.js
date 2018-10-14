import Vue from 'vue'
import Router from 'vue-router'
import Mainpage from '../components/mainpage/mainpage'
import Findmore from '../components/findmore/findmore'
import Myself from '../components/myself/myself'
import Notice from '../components/notice/notice'
import Search from '../components/search/search'
import ArticleDetail from '../components/article-detail/article-detail'

Vue.use(Router)

export default new Router({
  routes: [
      {
          path: '/',
          redirect: '/mainpage'
      },
      {
          path: '/mainpage',
          name: 'mainpage',
          component: Mainpage,
          children:[
              {
                  path: '../article-detail',
                  name: 'article-detail',
                  component: ArticleDetail
              }
          ]
      },
      {
          path: '/findmore',
          name: 'findmore',
          component: Findmore
      },
      {
          path: '/myself',
          name: 'myself',
          component: Myself
      },
      {
          path: '/notice',
          name: 'notice',
          component: Notice
      },
      {
          path: '/search',
          name: 'search',
          component: Search
      },
      {
          path: '/article-detail/:book_id',
          name: 'article-detail',
          component: ArticleDetail
      }
  ]
})
