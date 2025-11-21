import { DataViewLayout } from "@/components/data-view-layout"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import { Badge } from "@/components/ui/badge"

export default function ReceiptsPage() {
  const receipts = [
    { id: "1", receiptNo: "RCP-001", date: "2024-01-15", amount: "$500", type: "Tithe", member: "John Doe" },
    { id: "2", receiptNo: "RCP-002", date: "2024-01-16", amount: "$250", type: "Offering", member: "Jane Smith" },
    { id: "3", receiptNo: "RCP-003", date: "2024-01-17", amount: "$1000", type: "Pledge", member: "Bob Johnson" },
  ]

  const listContent = (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <div>
          <h3 className="text-lg font-medium">All Receipts</h3>
          <p className="text-sm text-muted-foreground">{receipts.length} total receipts</p>
        </div>
        <Button>
          <Plus className="size-4 mr-2" />
          New Receipt
        </Button>
      </div>
      <div className="rounded-md border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Receipt No</TableHead>
              <TableHead>Date</TableHead>
              <TableHead>Type</TableHead>
              <TableHead>Member</TableHead>
              <TableHead>Amount</TableHead>
              <TableHead className="text-right">Actions</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {receipts.map((receipt) => (
              <TableRow key={receipt.id}>
                <TableCell className="font-medium">{receipt.receiptNo}</TableCell>
                <TableCell>{receipt.date}</TableCell>
                <TableCell>
                  <Badge variant="outline">{receipt.type}</Badge>
                </TableCell>
                <TableCell>{receipt.member}</TableCell>
                <TableCell className="font-semibold">{receipt.amount}</TableCell>
                <TableCell className="text-right">
                  <Button variant="ghost" size="sm">
                    View
                  </Button>
                  <Button variant="ghost" size="sm">
                    Print
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
      Receipt analytics and trends will be displayed here
    </div>
  )

  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Receipts</h1>
        <p className="text-muted-foreground">Manage financial receipts and transactions</p>
      </div>
      <DataViewLayout
        title="Receipt Records"
        description="All financial receipts and their details"
        listContent={listContent}
        chartContent={chartContent}
      />
    </div>
  )
}
