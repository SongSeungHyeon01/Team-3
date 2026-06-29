import { Routes, Route } from "react-router-dom"
import UploadPage        from "./pages/UploadPage"
import SearchPage        from "./pages/SearchPage"
import DocumentDetailPage from "./pages/DocumentDetailPage"
import AdminPage         from "./pages/AdminPage"
export default function App() {
  return (
    <Routes>
      <Route path="/"              element={<SearchPage />} />
      <Route path="/upload"        element={<UploadPage />} />
      <Route path="/documents/:id" element={<DocumentDetailPage />} />
      <Route path="/admin"         element={<AdminPage />} />
    </Routes>
  )
}
