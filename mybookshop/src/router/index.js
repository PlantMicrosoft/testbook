import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import ProductDetail from '../views/ProductDetail.vue'
import ShoppingCart from '../views/ShoppingCart.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/product/:id',
      name: 'product-detail',
      component: ProductDetail,
    },
    {
      path: '/cart',
      name: 'shopping-cart',
      component: ShoppingCart,
    },
  ],
})

export default router
