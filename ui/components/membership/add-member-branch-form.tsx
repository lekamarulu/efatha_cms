"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { User, Building2, MapPin, Home, Calendar, Mail } from "lucide-react"

interface AddMemberBranchFormProps {
  onSuccess?: () => void
  onCancel?: () => void
}

export function AddMemberBranchForm({ onSuccess, onCancel }: AddMemberBranchFormProps) {
  const [formData, setFormData] = useState({
    memberRef: "",
    branchRef: "",
    startDate: "",
    endDate: "",
    churchZone: "",
    churchCell: "",
    streetResidence: "",
    houseNumber: "",
    residenceDetail: "",
    housingStatusId: "",
    postalAddress: "",
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    console.log("[v0] Form submitted:", formData)
    onSuccess?.()
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Member & Branch Information */}
      <Card>
        <CardHeader>
          <div className="flex items-center gap-2">
            <User className="size-5 text-primary" />
            <CardTitle>Member & Branch Assignment</CardTitle>
          </div>
          <CardDescription>Select the member and branch for this assignment</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="memberRef">Member Reference*</Label>
              <Select
                value={formData.memberRef}
                onValueChange={(value) => setFormData({ ...formData, memberRef: value })}
              >
                <SelectTrigger id="memberRef">
                  <SelectValue placeholder="Select member" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="MEM-001">MEM-001 - John Doe</SelectItem>
                  <SelectItem value="MEM-002">MEM-002 - Jane Smith</SelectItem>
                  <SelectItem value="MEM-003">MEM-003 - Bob Johnson</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="branchRef">Branch Reference*</Label>
              <Select
                value={formData.branchRef}
                onValueChange={(value) => setFormData({ ...formData, branchRef: value })}
              >
                <SelectTrigger id="branchRef">
                  <SelectValue placeholder="Select branch" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="BR-001">BR-001 - Main Branch</SelectItem>
                  <SelectItem value="BR-002">BR-002 - East Branch</SelectItem>
                  <SelectItem value="BR-003">BR-003 - West Branch</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Assignment Period */}
      <Card>
        <CardHeader>
          <div className="flex items-center gap-2">
            <Calendar className="size-5 text-primary" />
            <CardTitle>Assignment Period</CardTitle>
          </div>
          <CardDescription>Define the start and end dates for this assignment</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="startDate">Start Date*</Label>
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
              <p className="text-sm text-muted-foreground">Leave blank for ongoing assignment</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Church Location */}
      <Card>
        <CardHeader>
          <div className="flex items-center gap-2">
            <Building2 className="size-5 text-primary" />
            <CardTitle>Church Zone & Cell</CardTitle>
          </div>
          <CardDescription>Specify the church zone and cell information</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="churchZone">Church Zone</Label>
              <Select
                value={formData.churchZone}
                onValueChange={(value) => setFormData({ ...formData, churchZone: value })}
              >
                <SelectTrigger id="churchZone">
                  <SelectValue placeholder="Select zone" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Zone A">Zone A</SelectItem>
                  <SelectItem value="Zone B">Zone B</SelectItem>
                  <SelectItem value="Zone C">Zone C</SelectItem>
                  <SelectItem value="Zone D">Zone D</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="churchCell">Church Cell</Label>
              <Select
                value={formData.churchCell}
                onValueChange={(value) => setFormData({ ...formData, churchCell: value })}
              >
                <SelectTrigger id="churchCell">
                  <SelectValue placeholder="Select cell" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Cell 1">Cell 1</SelectItem>
                  <SelectItem value="Cell 2">Cell 2</SelectItem>
                  <SelectItem value="Cell 3">Cell 3</SelectItem>
                  <SelectItem value="Cell 4">Cell 4</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Residential Information */}
      <Card>
        <CardHeader>
          <div className="flex items-center gap-2">
            <Home className="size-5 text-primary" />
            <CardTitle>Residential Information</CardTitle>
          </div>
          <CardDescription>Provide the member's residential address details</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="streetResidence">Street Address</Label>
              <div className="relative">
                <MapPin className="absolute left-3 top-3 size-4 text-muted-foreground" />
                <Input
                  id="streetResidence"
                  placeholder="123 Faith Street"
                  value={formData.streetResidence}
                  onChange={(e) => setFormData({ ...formData, streetResidence: e.target.value })}
                  className="pl-9"
                />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="houseNumber">House Number</Label>
              <div className="relative">
                <Home className="absolute left-3 top-3 size-4 text-muted-foreground" />
                <Input
                  id="houseNumber"
                  placeholder="A-101"
                  value={formData.houseNumber}
                  onChange={(e) => setFormData({ ...formData, houseNumber: e.target.value })}
                  className="pl-9"
                />
              </div>
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="postalAddress">Postal Address</Label>
            <div className="relative">
              <Mail className="absolute left-3 top-3 size-4 text-muted-foreground" />
              <Input
                id="postalAddress"
                placeholder="P.O. Box 1234"
                value={formData.postalAddress}
                onChange={(e) => setFormData({ ...formData, postalAddress: e.target.value })}
                className="pl-9"
              />
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="housingStatusId">Housing Status</Label>
            <Select
              value={formData.housingStatusId}
              onValueChange={(value) => setFormData({ ...formData, housingStatusId: value })}
            >
              <SelectTrigger id="housingStatusId">
                <SelectValue placeholder="Select housing status" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="owner">Owner</SelectItem>
                <SelectItem value="renter">Renter</SelectItem>
                <SelectItem value="family">Living with Family</SelectItem>
                <SelectItem value="other">Other</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <div className="space-y-2">
            <Label htmlFor="residenceDetail">Additional Residence Details</Label>
            <Textarea
              id="residenceDetail"
              placeholder="Enter any additional details about the residence..."
              value={formData.residenceDetail}
              onChange={(e) => setFormData({ ...formData, residenceDetail: e.target.value })}
              rows={3}
            />
          </div>
        </CardContent>
      </Card>

      {/* Submit Buttons */}
      <div className="flex justify-end gap-3">
        <Button type="button" variant="outline" onClick={onCancel}>
          Cancel
        </Button>
        <Button type="submit">Save Assignment</Button>
      </div>
    </form>
  )
}
