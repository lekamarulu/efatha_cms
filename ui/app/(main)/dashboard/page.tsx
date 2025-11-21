import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Users, DollarSign, Box, TrendingUp, Activity } from "lucide-react"

export default function DashboardPage() {
  const stats = [
    {
      title: "Total Members",
      value: "1,245",
      change: "+12.5%",
      icon: Users,
      color: "text-blue-600",
    },
    {
      title: "Total Revenue",
      value: "$45,231",
      change: "+8.2%",
      icon: DollarSign,
      color: "text-green-600",
    },
    {
      title: "Total Assets",
      value: "234",
      change: "+5.4%",
      icon: Box,
      color: "text-purple-600",
    },
    {
      title: "Active Projects",
      value: "12",
      change: "+2",
      icon: Activity,
      color: "text-orange-600",
    },
  ]

  return (
    <div className="space-y-4">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Dashboard</h1>
        <p className="text-muted-foreground">Overview of your church management system</p>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.title}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">{stat.title}</CardTitle>
              <stat.icon className={`size-4 ${stat.color}`} />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stat.value}</div>
              <p className="text-xs text-muted-foreground flex items-center gap-1">
                <TrendingUp className="size-3 text-green-600" />
                {stat.change} from last month
              </p>
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        <Card className="cursor-pointer hover:shadow-md transition-shadow">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Users className="size-5" />
              Membership Dashboard
            </CardTitle>
            <CardDescription>View detailed membership statistics and analytics</CardDescription>
          </CardHeader>
          <CardContent>
            <a href="/dashboard/membership" className="text-sm text-primary hover:underline">
              View Details →
            </a>
          </CardContent>
        </Card>

        <Card className="cursor-pointer hover:shadow-md transition-shadow">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <DollarSign className="size-5" />
              Finance Dashboard
            </CardTitle>
            <CardDescription>Track financial performance and transactions</CardDescription>
          </CardHeader>
          <CardContent>
            <a href="/dashboard/finance" className="text-sm text-primary hover:underline">
              View Details →
            </a>
          </CardContent>
        </Card>

        <Card className="cursor-pointer hover:shadow-md transition-shadow">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Box className="size-5" />
              Assets Dashboard
            </CardTitle>
            <CardDescription>Monitor church assets and their locations</CardDescription>
          </CardHeader>
          <CardContent>
            <a href="/dashboard/assets" className="text-sm text-primary hover:underline">
              View Details →
            </a>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
