import axios from "axios"
export const api = axios.create({ baseURL: "/api" })
export const search      = (body) => api.post("/search", body).then(r => r.data)
export const uploadFiles = (form) => api.post("/upload", form)
export const getStatus   = (id)  => api.get(`/upload/${id}/status`).then(r => r.data)
export const getDocument = (id)  => api.get(`/documents/${id}`).then(r => r.data)
export const getHistory  = (id)  => api.get(`/documents/${id}/history`).then(r => r.data)
