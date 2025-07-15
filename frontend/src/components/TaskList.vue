<template>
  <ul class="space-y-2">
    <li
      v-for="task in tasks"
      :key="task.id"
      class="flex justify-between items-center border py-2 px-3 bg-white rounded-lg shadow"
    >
      <span>{{ task.title }}</span>
      <button
        @click="deleteTask(task.id)"
        class="bg-red-500 text-white px-2 py-1 rounded text-sm"
      >
        Delete
      </button>
    </li>
  </ul>
</template>

<script setup>
import api from '../api'
import { toast } from 'vue3-toastify'

const props = defineProps({ tasks: Array })
const emit = defineEmits(['task-deleted'])

async function deleteTask(id) {
  try {
    await api.delete(`/tasks/${id}`)
    toast.success('Task deleted!')
    emit('task-deleted')
  } catch (err) {
    toast.error('Failed to delete task')
    console.error('Delete failed:', err)
  }
}
</script>
