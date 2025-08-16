import ReactFlow, { MiniMap, Controls, Background } from 'react-flow-renderer'

const initialNodes = [
	{ id: 'start', position: { x: 50, y: 50 }, data: { label: 'Start' }, type: 'input' },
	{ id: 'say1', position: { x: 250, y: 50 }, data: { label: 'Say: Hello' } },
	{ id: 'end', position: { x: 450, y: 50 }, data: { label: 'End' }, type: 'output' },
]

const initialEdges = [
	{ id: 'e1', source: 'start', target: 'say1' },
	{ id: 'e2', source: 'say1', target: 'end' },
]

export default function WorkflowCanvas() {
	return (
		<div style={{ height: 600 }} className="bg-white rounded shadow">
			<ReactFlow nodes={initialNodes} edges={initialEdges} fitView>
				<MiniMap />
				<Controls />
				<Background />
			</ReactFlow>
		</div>
	)
}