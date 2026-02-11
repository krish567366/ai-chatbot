import { useEffect, useState } from 'react'
import axios from 'axios'

type Agent = {
	id: number
	name: string
	locale: string
	voice: string
}

export default function AgentsList() {
	const [agents, setAgents] = useState<Agent[]>([])
	const [name, setName] = useState('')

	useEffect(() => {
		axios.get('/api/v1/agents/').then(r => setAgents(r.data))
	}, [])

	async function createAgent() {
		const r = await axios.post('/api/v1/agents/', { name })
		setAgents(a => [...a, r.data])
		setName('')
	}

	return (
		<div className="space-y-4">
			<h1 className="text-2xl font-semibold">Agents</h1>
			<div className="flex gap-2">
				<input className="border px-2 py-1" value={name} onChange={e => setName(e.target.value)} placeholder="Agent name" />
				<button className="bg-blue-600 text-white px-3 py-1 rounded" onClick={createAgent} disabled={!name}>Create</button>
			</div>
			<ul className="divide-y bg-white rounded shadow">
				{agents.map(a => (
					<li key={a.id} className="p-3 flex justify-between">
						<span>{a.name}</span>
						<span className="text-sm text-gray-500">{a.locale} • {a.voice}</span>
					</li>
				))}
			</ul>
		</div>
	)
}