"use client"

import { useState } from "react"
import { DataViewLayout } from "@/components/data-view-layout"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Plus, MapPin, Home, BarChart3 } from "lucide-react"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { AddMemberBranchForm } from "@/components/membership/add-member-branch-form"

export default function MemberBranchPage() {
  const [isDialogOpen, setIsDialogOpen] = useState(false)

  const memberBranches = [
    {
      id: "1",
      memberRef: "MEM-001",
      memberName: "John Doe",
      branchRef: "BR-001",
      branchName: "Main Branch",
      startDate: "2024-01-15",
      endDate: null,
      churchZone: "Zone A",
      churchCell: "Cell 1",
      streetResidence: "123 Faith Street",
      houseNumber: "A-101",
      postalAddress: "P.O. Box 1234",
      housingStatus: "Owner",
    },
    {
      id: "2",
      memberRef: "MEM-002",
      memberName: "Jane Smith",
      branchRef: "BR-002",
      branchName: "East Branch",
      startDate: "2023-06-20",
      endDate: "2024-12-31",
      churchZone: "Zone B",
      churchCell: "Cell 3",
      streetResidence: "456 Grace Avenue",
      houseNumber: "B-205",
      postalAddress: "P.O. Box 5678",
      housingStatus: "Renter",
    },
    {
      id: "3",
      memberRef: "MEM-003",
      memberName: "Bob Johnson",
      branchRef: "BR-001",
      branchName: "Main Branch",
      startDate: "2024-03-10",
      endDate: null,
      churchZone: "Zone A",
      churchCell: "Cell 2",
      streetResidence: "789 Hope Boulevard",
      houseNumber: "C-312",
      postalAddress: "P.O. Box 9012",
      housingStatus: "Owner",
    },
  ]

  const listContent = (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-medium">Member Branch Assignments</h3>
          <p className="text-sm text-muted-foreground">{memberBranches.length} total assignments</p>
        </div>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button>
              <Plus className="size-4 mr-2" />
              Add Assignment
            </Button>
          </DialogTrigger>
          <DialogContent className="max-w-3xl max-h-[90vh] overflow-y-auto">
            <DialogHeader>
              <DialogTitle>Add Member Branch Assignment</DialogTitle>
              <DialogDescription>
                Create a new branch assignment for a member with residential details
              </DialogDescription>
            </DialogHeader>
            <AddMemberBranchForm onSuccess={() => setIsDialogOpen(false)} onCancel={() => setIsDialogOpen(false)} />
          </DialogContent>
        </Dialog>
      </div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Member</TableHead>
              <TableHead>Branch</TableHead>
              <TableHead>Zone/Cell</TableHead>
              <TableHead>Residence</TableHead>
              <TableHead>Period</TableHead>
              <TableHead>Status</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {memberBranches.map((assignment) => (
              <TableRow key={assignment.id}>
                <TableCell>
                  <div>
                    <p className="font-medium">{assignment.memberName}</p>
                    <p className="text-sm text-muted-foreground">{assignment.memberRef}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <div>
                    <p className="font-medium">{assignment.branchName}</p>
                    <p className="text-sm text-muted-foreground">{assignment.branchRef}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <div className="space-y-1">
                    <div className="flex items-center gap-1 text-sm">
                      <MapPin className="size-3" />
                      {assignment.churchZone}
                    </div>
                    <div className="text-sm text-muted-foreground">{assignment.churchCell}</div>
                  </div>
                </TableCell>
                <TableCell>
                  <div className="max-w-[200px]">
                    <div className="flex items-center gap-1 text-sm">
                      <Home className="size-3" />
                      {assignment.houseNumber}
                    </div>
                    <p className="text-sm text-muted-foreground truncate">{assignment.streetResidence}</p>
                  </div>
                </TableCell>
                <TableCell>
                  <div className="text-sm">
                    <p>{new Date(assignment.startDate).toLocaleDateString()}</p>
                    {assignment.endDate && (
                      <p className="text-muted-foreground">to {new Date(assignment.endDate).toLocaleDateString()}</p>
                    )}
                  </div>
                </TableCell>
                <TableCell>
                  <Badge variant={assignment.endDate ? "secondary" : "default"}>
                    {assignment.endDate ? "Ended" : "Active"}
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
        <p>Member branch distribution charts will be displayed here</p>
        <p className="text-sm">View statistics by zone, cell, and housing status</p>
      </div>
    </div>
  )

  return (
    <div className="space-y-4 p-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Member Branch Assignments</h1>
        <p className="text-muted-foreground">Manage member branch assignments and residential information</p>
      </div>
      <DataViewLayout
        title="Branch Assignment List"
        description="Complete list of all member branch assignments with residential details"
        listContent={listContent}
        chartContent={chartContent}
      />
    </div>
  )
}
