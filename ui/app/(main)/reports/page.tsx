import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { FileText, Download, Users, DollarSign, Box, BarChart3 } from "lucide-react"

export default function ReportsPage() {
  const reportCategories = [
    {
      title: "Membership Reports",
      icon: Users,
      reports: ["Member Directory", "Attendance Records", "New Members Report", "Membership Growth Analysis"],
    },
    {
      title: "Financial Reports",
      icon: DollarSign,
      reports: ["Income Statement", "Balance Sheet", "Cash Flow Statement", "Pledge Reports", "Receipt Summary"],
    },
    {
      title: "Asset Reports",
      icon: Box,
      reports: ["Asset Inventory", "Asset Movement History", "Asset Valuation Report", "Location Assignment Report"],
    },
    {
      title: "Statistical Reports",
      icon: BarChart3,
      reports: [
        "Church Growth Statistics",
        "Demographic Analysis",
        "Department Activity Report",
        "Ministry Participation Report",
      ],
    },
  ]

  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Reports</h1>
        <p className="text-muted-foreground">Generate and download system reports in PDF and DOCX formats</p>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        {reportCategories.map((category) => (
          <Card key={category.title}>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <category.icon className="size-5" />
                {category.title}
              </CardTitle>
              <CardDescription>Available reports for {category.title.toLowerCase()}</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                {category.reports.map((report) => (
                  <div key={report} className="flex items-center justify-between p-2 rounded-md hover:bg-accent">
                    <div className="flex items-center gap-2">
                      <FileText className="size-4 text-muted-foreground" />
                      <span className="text-sm">{report}</span>
                    </div>
                    <div className="flex gap-1">
                      <Button variant="ghost" size="sm">
                        <Download className="size-4 mr-1" />
                        PDF
                      </Button>
                      <Button variant="ghost" size="sm">
                        <Download className="size-4 mr-1" />
                        DOCX
                      </Button>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  )
}
