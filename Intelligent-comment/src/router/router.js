import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/myheader/myheader'
import ArticleList from '../components/article-list/article-list'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
      {
          path: '/',
          name: 'article-list',
          component: ArticleList
      }
  ]
})
