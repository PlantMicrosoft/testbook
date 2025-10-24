<template>
  <div class="min-h-screen bg-gray-50 flex flex-col">
    <header class="bg-white border-b border-gray-200 px-6 py-4">
      <div class="flex items-center justify-between">
        <h1 class="text-2xl font-bold">我的书店</h1>
        <div class="flex items-center gap-4 flex-1 max-w-3xl mx-8">
          <input
            type="search"
            placeholder="search"
            class="flex-1 px-4 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button class="px-6 py-2 border border-gray-900 rounded hover:bg-gray-100">查询</button>
        </div>
        <div class="flex items-center gap-4">
          <div class="flex items-center gap-2 px-3 py-1 border border-gray-900 rounded">
            <span class="font-semibold">￥19.99</span>
            <span class="bg-gray-200 px-2 py-0.5 rounded text-sm">2</span>
          </div>
          <button class="text-2xl">🛒</button>
        </div>
      </div>
    </header>

    <div class="flex flex-1 relative">
      <aside
        :style="{ width: sidebarWidth + 'px' }"
        class="bg-blue-50 border-r border-gray-300 flex-shrink-0 relative"
      >
        <div class="p-6">
          <h2 class="text-lg font-semibold mb-4">按目录采购</h2>
          <nav class="space-y-2">
            <a href="#" class="block text-blue-600 hover:underline">书籍</a>
            <a href="#" class="block text-blue-600 hover:underline">咖啡杯</a>
            <a href="#" class="block text-blue-600 hover:underline">鼠标垫</a>
          </nav>
        </div>

        <div
          @mousedown="startResize"
          class="absolute top-0 right-0 w-1 h-full cursor-col-resize hover:bg-blue-400 transition-colors group"
        >
          <div
            class="absolute top-1/2 right-0 w-1 h-12 bg-gray-400 group-hover:bg-blue-500 transition-colors"
          ></div>
        </div>
      </aside>

      <main class="flex-1 p-8">
        <div class="max-w-3xl">
          <h2 class="text-2xl font-bold mb-6">购物车详细</h2>

          Cart Items
          <div class="space-y-4 mb-8">
            <div
              v-for="item in cartItems"
              :key="item.id"
              class="bg-white border border-gray-200 rounded p-4"
            >
              <div class="flex gap-4">
                <div class="w-20 h-20 bg-gray-100 flex-shrink-0 flex items-center justify-center">
                  <svg
                    class="w-10 h-10 text-gray-300"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"
                    />
                  </svg>
                </div>
                <div class="flex-1">
                  <h3 class="font-semibold">{{ item.title }}</h3>
                  <p class="text-gray-600 text-sm">{{ item.subtitle }}</p>
                  <p class="font-bold mt-1">{{ item.price }}</p>
                </div>
                <div class="flex flex-col items-end gap-2">
                  <div class="flex items-center gap-2">
                    <span class="text-sm">Quantity</span>
                    <select class="border border-gray-300 rounded px-2 py-1">
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                    </select>
                  </div>
                  <p class="text-sm">
                    Sub-total <span class="font-semibold">{{ item.price }}</span>
                  </p>
                  <button
                    class="px-4 py-1 border border-gray-900 rounded hover:bg-gray-100 text-sm"
                  >
                    Remove
                  </button>
                </div>
              </div>
            </div>
          </div>

          订单总结
          <div class="bg-white border border-gray-200 rounded p-6">
            <div class="border-t border-gray-300 pt-4 space-y-3">
              <div class="flex justify-between">
                <span class="font-semibold">总数量:</span>
                <span class="font-semibold">2</span>
              </div>
              <div class="flex justify-between">
                <span class="font-semibold">运货:</span>
                <span class="font-semibold">FREE</span>
              </div>
              <div class="flex justify-between text-xl">
                <span class="font-bold">总价格:</span>
                <span class="font-bold">￥19.99</span>
              </div>
              <button
                class="w-full mt-4 px-6 py-3 bg-gray-900 text-white rounded hover:bg-gray-800 font-semibold"
              >
                检出
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>

    <footer class="bg-white border-t border-gray-200 py-4">
      <div class="flex justify-center gap-6 text-sm">
        <a href="#" class="hover:underline">关于我们</a>
        <a href="#" class="hover:underline">联系我们</a>
        <a href="#" class="hover:underline">寻求帮助</a>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onUnmounted } from 'vue'

const sidebarWidth = ref(200)
const isResizing = ref(false)

const cartItems = ref([
  {
    id: 1,
    title: '产品名称',
    subtitle: '产品小说明',
    price: '￥9.99',
  },
  {
    id: 2,
    title: '产品名称',
    subtitle: '产品小说明',
    price: '￥10.99',
  },
])

const startResize = (e) => {
  isResizing.value = true
  document.addEventListener('mousemove', handleResize)
  document.addEventListener('mouseup', stopResize)
  e.preventDefault()
}

const handleResize = (e) => {
  if (isResizing.value) {
    const newWidth = e.clientX
    if (newWidth >= 150 && newWidth <= 400) {
      sidebarWidth.value = newWidth
    }
  }
}

const stopResize = () => {
  isResizing.value = false
  document.removeEventListener('mousemove', handleResize)
  document.removeEventListener('mouseup', stopResize)
}

onUnmounted(() => {
  document.removeEventListener('mousemove', handleResize)
  document.removeEventListener('mouseup', stopResize)
})
</script>
