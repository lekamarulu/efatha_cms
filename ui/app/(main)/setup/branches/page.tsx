import { DataViewLayout } from "@/components/data-view-layout"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"

export default function BranchesPage() {
  const branches = [
    { id: "1", ref: "BRN-001", name: "Main Branch", region: "Central", dateCreated: "2020-01-01" },
    { id: "2", ref: "BRN-002", name: "East Branch", region: "Eastern", dateCreated: "2021-03-15" },
    { id: "3", ref: "BRN-003", name: "West Branch", region: "Western", dateCreated: "2022-06-20" },
  ]

  const listContent = (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-medium">All Branches</h3>
          <p className="text-sm text-muted-foreground">{branches.length} total branches</p>
        </div>
        <Button>
          <Plus className="size-4 mr-2" />
          Add Branch
        </Button>
      </div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Reference</TableHead>
              <TableHead>Branch Name</TableHead>
              <TableHead>Region</TableHead>
              <TableHead>Date Created</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {branches.map((branch) => (
              <TableRow key={branch.id}>
                <TableCell className="font-medium">{branch.ref}</TableCell>
                <TableCell>{branch.name}</TableCell>
                <TableCell>{branch.region}</TableCell>
                <TableCell>{branch.dateCreated}</TableCell>
                <TableCell className="text-right">
                  <Button variant="ghost" size="sm">
                    Edit
                  </Button>
                  <Button variant="ghost" size="sm">
                    View
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
      Branch statistics and growth charts will be displayed here
    </div>
  )

  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Branches</h1>
        <p className="text-muted-foreground">Manage church branches and locations</p>
      </div>
      <DataViewLayout
        title="Branch Directory"
        description="All church branches and their information"
        listContent={listContent}
        chartContent={chartContent}
      />
    </div>
  )
}
