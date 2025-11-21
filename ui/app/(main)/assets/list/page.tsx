import { DataViewLayout } from "@/components/data-view-layout"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import { Badge } from "@/components/ui/badge"

export default function AssetsListPage() {
  const assets = [
    {
      id: "1",
      code: "AST-001",
      description: "Projector",
      category: "Electronics",
      location: "Main Hall",
      status: "Active",
    },
    {
      id: "2",
      code: "AST-002",
      description: "Sound System",
      category: "Electronics",
      location: "Sanctuary",
      status: "Active",
    },
    {
      id: "3",
      code: "AST-003",
      description: "Office Desk",
      category: "Furniture",
      location: "Admin Office",
      status: "Active",
    },
  ]

  const listContent = (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-medium">All Assets</h3>
          <p className="text-sm text-muted-foreground">{assets.length} total assets</p>
        </div>
        <Button>
          <Plus className="size-4 mr-2" />
          Add Asset
        </Button>
      </div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Asset Code</TableHead>
              <TableHead>Description</TableHead>
              <TableHead>Category</TableHead>
              <TableHead>Location</TableHead>
              <TableHead>Status</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {assets.map((asset) => (
              <TableRow key={asset.id}>
                <TableCell className="font-medium">{asset.code}</TableCell>
                <TableCell>{asset.description}</TableCell>
                <TableCell>{asset.category}</TableCell>
                <TableCell>{asset.location}</TableCell>
                <TableCell>
                  <Badge variant={asset.status === "Active" ? "default" : "secondary"}>{asset.status}</Badge>
                </TableCell>
                <TableCell className="text-right">
                  <Button variant="ghost" size="sm">
                    Edit
                  </Button>
                  <Button variant="ghost" size="sm">
                    Move
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  )

  const chartContent = (
    <div className="h-[400px] flex items-center justify-center text-muted-foreground">
      Asset distribution charts will be displayed here
    </div>
  )

  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Assets</h1>
        <p className="text-muted-foreground">Manage church assets and equipment</p>
      </div>
      <DataViewLayout
        title="Asset Inventory"
        description="Complete inventory of all church assets"
        listContent={listContent}
        chartContent={chartContent}
      />
    </div>
  )
}
