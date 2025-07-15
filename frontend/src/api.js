import axios from 'axios'

const api = axios.create({
  baseURL: 'https://task-api-frosty-sea-8995.fly.dev'
})

export default api