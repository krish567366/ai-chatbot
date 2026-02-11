import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import './index.css'
import AgentsList from './pages/AgentsList'
import WorkflowCanvas from './pages/WorkflowCanvas'
import CallMonitor from './pages/CallMonitor'

function App() {
	return (
		<BrowserRouter>
			<div className="min-h-screen bg-gray-50 text-gray-900">
				<nav className="p-4 bg-white shadow flex gap-4">
					<Link to="/agents">Agents</Link>
					<Link to="/workflows">Workflows</Link>
					<Link to="/calls">Calls</Link>
				</nav>
				<main className="p-4">
					<Routes>
						<Route path="/agents" element={<AgentsList />} />
						<Route path="/workflows" element={<WorkflowCanvas />} />
						<Route path="/calls" element={<CallMonitor />} />
						<Route path="*" element={<AgentsList />} />
					</Routes>
				</main>
			</div>
		</BrowserRouter>
	)
}

ReactDOM.createRoot(document.getElementById('root')!).render(
	<React.StrictMode>
		<App />
	</React.StrictMode>
)