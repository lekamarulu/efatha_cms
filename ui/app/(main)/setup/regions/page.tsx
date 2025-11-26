import { DataViewLayout } from "@/components/data-view-layout"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"

export default function RegionsPage() {
  const Regions = [
    {
      id: "1",
      name: "John Doe",
      gender: "Male",
      email: "john@example.com",
      phone: "+1234567890",
      branch: "Main Branch",
    },
    {
      id: "2",
      name: "Jane Smith",
      gender: "Female",
      email: "jane@example.com",
      phone: "+1234567891",
      branch: "East Branch",
    },
    {
      id: "3",
      name: "Bob Johnson",
      gender: "Male",
      email: "bob@example.com",
      phone: "+1234567892",
      branch: "West Branch",
    },
  ]

  const listContent = (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-medium">All Regions</h3>
          <p className="text-sm text-muted-foreground">{Regions.length} total Regions</p>
        </div>
        <Button>
          <Plus className="size-4 mr-2" />
          Add Member
        </Button>
      </div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Name</TableHead>
              <TableHead>Gender</TableHead>
              <TableHead>Email</TableHead>
              <TableHead>Phone</TableHead>
              <TableHead>Branch</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {Regions.map((member) => (
              <TableRow key={member.id}>
                <TableCell className="font-medium">{member.name}</TableCell>
                <TableCell>{member.gender}</TableCell>
                <TableCell>{member.email}</TableCell>
                <TableCell>{member.phone}</TableCell>
                <TableCell>{member.branch}</TableCell>
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
      Member distribution charts will be displayed here
    </div>
  )

  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Regions</h1>
        <p className="text-muted-foreground">Manage and view all Regions</p>
      </div>
      <DataViewLayout
        title="Region List"
        description="Complete list of all registered Regions"
        listContent={listContent}
      />
    </div>
  )
}
