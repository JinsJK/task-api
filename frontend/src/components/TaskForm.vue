<template>
  <form @submit.prevent="addTask" class="mb-6">
    <input
      v-model="title"
      placeholder="New task..."
      class="border rounded p-2 w-3/4 mr-2"
    />
    <button class="bg-blue-500 text-white px-4 py-2 rounded">Add</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import api from '../api'
import { toast } from 'vue3-toastify'

const emit = defineEmits(['task-added'])
const title = ref('')

async function addTask() {
  if (!title.value.trim()) return

  try {
    await api.post('/tasks', { title: title.value })
    toast.success('Task added!')          // ✅ success toast
    title.value = ''
    emit('task-added')
  } catch (error) {
    toast.error('Failed to add task')     // ❌ error toast
    console.error('Failed to add task:', error)
  }
}
</script>
