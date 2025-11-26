"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { User, Briefcase, Calendar } from "lucide-react"
import { Checkbox } from "@/components/ui/checkbox"

interface AddChurchPositionFormProps {
  onSuccess?: () => void
  onCancel?: () => void
}

export function AddChurchPositionForm({ onSuccess, onCancel }: AddChurchPositionFormProps) {
  const [formData, setFormData] = useState({
    memberId: "",
    branchId: "",
    positionId: "",
    startDate: "",
    endDate: "",
    isActive: true,
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log("Form submitted:", formData)
    onSuccess?.()
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Member & Branch Selection */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg flex items-center gap-2">
            <User className="size-5" />
            Member & Branch
          </CardTitle>
          <CardDescription>Select the member and branch for this position assignment</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="member">Member *</Label>
              <Select
                value={formData.memberId}
                onValueChange={(value) => setFormData({ ...formData, memberId: value })}
              >
                <SelectTrigger id="member">
                  <SelectValue placeholder="Select member" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="mem-001">John Doe (MEM-001)</SelectItem>
                  <SelectItem value="mem-002">Jane Smith (MEM-002)</SelectItem>
                  <SelectItem value="mem-003">Bob Johnson (MEM-003)</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="branch">Branch *</Label>
              <Select
                value={formData.branchId}
                onValueChange={(value) => setFormData({ ...formData, branchId: value })}
              >
                <SelectTrigger id="branch">
                  <SelectValue placeholder="Select branch" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="br-001">Main Branch (BR-001)</SelectItem>
                  <SelectItem value="br-002">East Branch (BR-002)</SelectItem>
                  <SelectItem value="br-003">West Branch (BR-003)</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Position Selection */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg flex items-center gap-2">
            <Briefcase className="size-5" />
            Position Details
          </CardTitle>
          <CardDescription>Select the church position for this assignment</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="position">Church Position *</Label>
            <Select
              value={formData.positionId}
              onValueChange={(value) => setFormData({ ...formData, positionId: value })}
            >
              <SelectTrigger id="position">
                <SelectValue placeholder="Select position" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="pos-001">Pastor</SelectItem>
                <SelectItem value="pos-002">Associate Pastor</SelectItem>
                <SelectItem value="pos-003">Youth Pastor</SelectItem>
                <SelectItem value="pos-004">Worship Leader</SelectItem>
                <SelectItem value="pos-005">Elder</SelectItem>
                <SelectItem value="pos-006">Deacon</SelectItem>
                <SelectItem value="pos-007">Children's Ministry Director</SelectItem>
                <SelectItem value="pos-008">Administrative Assistant</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </CardContent>
      </Card>

      {/* Assignment Period */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg flex items-center gap-2">
            <Calendar className="size-5" />
            Assignment Period
          </CardTitle>
          <CardDescription>Specify when this position assignment starts and ends</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="space-y-2">
              <Label htmlFor="startDate">Start Date *</Label>
              <Input
                id="startDate"
                type="date"
                value={formData.startDate}
                onChange={(e) => setFormData({ ...formData, startDate: e.target.value })}
                required
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="endDate">End Date</Label>
              <Input
                id="endDate"
                type="date"
                value={formData.endDate}
                onChange={(e) => setFormData({ ...formData, endDate: e.target.value })}
              />
              <p className="text-xs text-muted-foreground">Leave blank for ongoing assignment</p>
            </div>
          </div>
          <div className="flex items-center space-x-2">
            <Checkbox
              id="isActive"
              checked={formData.isActive}
              onCheckedChange={(checked) => setFormData({ ...formData, isActive: checked as boolean })}
            />
            <Label htmlFor="isActive" className="text-sm font-normal cursor-pointer">
              Mark as active position
            </Label>
          </div>
        </CardContent>
      </Card>

      {/* Form Actions */}
      <div className="flex justify-end gap-3">
        <Button type="button" variant="outline" onClick={onCancel}>
          Cancel
        </Button>
        <Button type="submit">Add Position Assignment</Button>
      </div>
    </form>
  )
}
