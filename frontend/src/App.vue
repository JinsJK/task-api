<template>
  <main class="max-w-xl mx-auto py-10 px-4">
    <h1 class="text-2xl font-bold mb-6">Task Manager</h1>
    
    <TaskForm @task-added="fetchTasks" />

    <div v-if="loading" class="text-gray-500 mt-4">Loading tasks...</div>
    <div v-else-if="tasks.length === 0" class="text-gray-400 mt-4">No tasks yet. 🎉</div>
    <TaskList v-else :tasks="tasks" @task-deleted="fetchTasks" />
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from './api'
import TaskForm from './components/TaskForm.vue'
import TaskList from './components/TaskList.vue'

const tasks = ref([])
const loading = ref(false)

async function fetchTasks() {
  loading.value = true
  try {
    const res = await api.get('/tasks')
    tasks.value = res.data
  } catch (e) {
    console.error('Error fetching tasks:', e)
  } finally {
    loading.value = false
  }
}

onMounted(fetchTasks)
</script>
