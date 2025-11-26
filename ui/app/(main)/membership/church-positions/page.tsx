"use client"

import { useState } from "react"
import { DataViewLayout } from "@/components/data-view-layout"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Plus, Briefcase, Calendar, BarChart3 } from "lucide-react"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { AddChurchPositionForm } from "@/components/church-positions/add-church-position-form"

export default function ChurchPositionsPage() {
  const [isDialogOpen, setIsDialogOpen] = useState(false)

  const churchPositions = [
    {
      id: "1",
      memberRef: "MEM-001",
      memberName: "John Doe",
      branchRef: "BR-001",
      branchName: "Main Branch",
      positionName: "Pastor",
      startDate: "2023-01-15",
      endDate: null,
      isActive: true,
    },
    {
      id: "2",
      memberRef: "MEM-002",
      memberName: "Jane Smith",
      branchRef: "BR-002",
      branchName: "East Branch",
      positionName: "Worship Leader",
      startDate: "2023-06-01",
      endDate: "2024-12-31",
      isActive: false,
    },
    {
      id: "3",
      memberRef: "MEM-003",
      memberName: "Bob Johnson",
      branchRef: "BR-001",
      branchName: "Main Branch",
      positionName: "Youth Pastor",
      startDate: "2024-01-01",
      endDate: null,
      isActive: true,
    },
    {
      id: "4",
      memberRef: "MEM-004",
      memberName: "Sarah Williams",
      branchRef: "BR-003",
      branchName: "West Branch",
      positionName: "Children's Ministry Director",
      startDate: "2023-09-15",
      endDate: null,
      isActive: true,
    },
    {
      id: "5",
      memberRef: "MEM-005",
      memberName: "Michael Brown",
      branchRef: "BR-002",
      branchName: "East Branch",
      positionName: "Elder",
      startDate: "2022-03-20",
      endDate: "2024-03-20",
      isActive: false,
    },
  ]

  const listContent = (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-medium">Church Position Assignments</h3>
          <p className="text-sm text-muted-foreground">
            {churchPositions.length} total positions ({churchPositions.filter((p) => p.isActive).length} active)
          </p>
        </div>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button>
              <Plus className="size-4 mr-2" />
              Add Position
            </Button>
          </DialogTrigger>
          <DialogContent className="max-w-2xl max-h-[90vh] overflow-y-auto">
            <DialogHeader>
              <DialogTitle>Add Church Position Assignment</DialogTitle>
              <DialogDescription>Assign a church position to a member at a specific branch</DialogDescription>
            </DialogHeader>
            <AddChurchPositionForm onSuccess={() => setIsDialogOpen(false)} onCancel={() => setIsDialogOpen(false)} />
          </DialogContent>
        </Dialog>
      </div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Member</TableHead>
              <TableHead>Position</TableHead>
              <TableHead>Branch</TableHead>
              <TableHead>Start Date</TableHead>
              <TableHead>End Date</TableHead>
              <TableHead>Status</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {churchPositions.map((position) => (
              <TableRow key={position.id}>
                <TableCell>
                  <div>
                    <p className="font-medium">{position.memberName}</p>
                    <p className="text-sm text-muted-foreground">{position.memberRef}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <div className="flex items-center gap-2">
                    <Briefcase className="size-4 text-muted-foreground" />
                    <span className="font-medium">{position.positionName}</span>
                  </div>
                </TableCell>
                <TableCell>
                  <div>
                    <p className="font-medium">{position.branchName}</p>
                    <p className="text-sm text-muted-foreground">{position.branchRef}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <div className="flex items-center gap-1 text-sm">
                    <Calendar className="size-3 text-muted-foreground" />
                    {new Date(position.startDate).toLocaleDateString()}
                  </div>
                </TableCell>
                <TableCell>
                  {position.endDate ? (
                    <div className="text-sm text-muted-foreground">
                      {new Date(position.endDate).toLocaleDateString()}
                    </div>
                  ) : (
                    <span className="text-sm text-muted-foreground">Ongoing</span>
                  )}
                </TableCell>
                <TableCell>
                  <Badge variant={position.isActive ? "default" : "secondary"}>
                    {position.isActive ? "Active" : "Inactive"}
                  </Badge>
                </TableCell>
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
      <div className="text-center space-y-2">
        <BarChart3 className="size-12 mx-auto opacity-50" />
        <p>Position distribution charts will be displayed here</p>
        <p className="text-sm">View statistics by position type, branch, and assignment duration</p>
      </div>
    </div>
  )

  return (
    <div className="space-y-4 p-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Church Position Assignments</h1>
        <p className="text-muted-foreground">Manage church position assignments across all branches</p>
      </div>
      <DataViewLayout
        title="Position Assignment List"
        description="Complete list of all church position assignments with member and branch details"
        listContent={listContent}
        chartContent={chartContent}
      />
    </div>
  )
}
