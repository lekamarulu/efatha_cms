"use client"

import type * as React from "react"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

interface DataViewLayoutProps {
  title: string
  description?: string
  listContent: React.ReactNode
  chartContent?: React.ReactNode
  graphContent?: React.ReactNode
}

export function DataViewLayout({ title, description, listContent, chartContent, graphContent }: DataViewLayoutProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        {description && <CardDescription>{description}</CardDescription>}
      </CardHeader>
      <CardContent>
        <Tabs defaultValue="list" className="w-full">
          <TabsList>
            <TabsTrigger value="list">List</TabsTrigger>
            {chartContent && <TabsTrigger value="charts">Charts</TabsTrigger>}
            {graphContent && <TabsTrigger value="graphs">Graphs</TabsTrigger>}
          </TabsList>
          <TabsContent value="list" className="mt-4">
            {listContent}
          </TabsContent>
          {chartContent && (
            <TabsContent value="charts" className="mt-4">
              {chartContent}
            </TabsContent>
          )}
          {graphContent && (
            <TabsContent value="graphs" className="mt-4">
              {graphContent}
            </TabsContent>
          )}
        </Tabs>
      </CardContent>
    </Card>
  )
}
