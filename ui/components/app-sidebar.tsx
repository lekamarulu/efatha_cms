// "use client"
// import {
//   LayoutDashboard,
//   Users,
//   DollarSign,
//   Box,
//   Settings,
//   FileText,
//   ChevronRight,
//   Church,
//   UserCircle,
//   Building2,
//   Briefcase,
//   GraduationCap,
//   MapPin,
//   Award,
//   CalendarDays,
//   CreditCard,
//   Wallet,
//   Receipt,
//   FolderTree,
//   PackageOpen,
//   Archive,
//   Globe,
//   Layers,
//   UserCog,
//   Target,
//   BookOpen,
// } from "lucide-react"

// import {
//   Sidebar,
//   SidebarContent,
//   SidebarGroup,
//   SidebarGroupContent,
//   SidebarGroupLabel,
//   SidebarMenu,
//   SidebarMenuButton,
//   SidebarMenuItem,
//   SidebarMenuSub,
//   SidebarMenuSubButton,
//   SidebarMenuSubItem,
//   SidebarHeader,
//   SidebarFooter,
// } from "@/components/ui/sidebar"
// import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible"

// const menuItems = [
//   {
//     title: "Dashboard",
//     icon: LayoutDashboard,
//     url: "/dashboard",
//     items: [
//       { title: "Membership", url: "/dashboard/membership", icon: Users },
//       { title: "Finance", url: "/dashboard/finance", icon: DollarSign },
//       { title: "Assets", url: "/dashboard/assets", icon: Box },
//     ],
//   },
//   {
//     title: "Membership",
//     icon: Users,
//     url: "/membership",
//     items: [
//       { title: "Members", url: "/membership/members", icon: UserCircle },
//       { title: "Branch Assignment", url: "/membership/member-branch", icon: Building2 },
//       { title: "Church Positions", url: "/membership/church-positions", icon: Award },
//       { title: "Department Leadership", url: "/membership/department-leadership", icon: Target },
//       { title: "Ministry Assignment", url: "/membership/ministry", icon: Church },
//       { title: "Education", url: "/membership/education", icon: GraduationCap },
//       { title: "Occupation", url: "/membership/occupation", icon: Briefcase },
//     ],
//   },
//   {
//     title: "Finance",
//     icon: DollarSign,
//     url: "/finance",
//     items: [
//       { title: "Financial Years", url: "/finance/years", icon: CalendarDays },
//       { title: "Payment Methods", url: "/finance/payment-methods", icon: CreditCard },
//       { title: "Accounts", url: "/finance/accounts", icon: Wallet },
//       { title: "Account Balances", url: "/finance/balances", icon: DollarSign },
//       { title: "Journal Entries", url: "/finance/journals", icon: BookOpen },
//       { title: "Receipts", url: "/finance/receipts", icon: Receipt },
//       { title: "Donors", url: "/finance/donors", icon: Users },
//       { title: "Projects", url: "/finance/projects", icon: FolderTree },
//       { title: "Pledges", url: "/finance/pledges", icon: FileText },
//     ],
//   },
//   {
//     title: "Assets",
//     icon: Box,
//     url: "/assets",
//     items: [
//       { title: "Locations", url: "/assets/locations", icon: MapPin },
//       { title: "Asset Categories", url: "/assets/categories", icon: Layers },
//       { title: "Asset Subcategories", url: "/assets/subcategories", icon: FolderTree },
//       { title: "Asset Index", url: "/assets/index", icon: Archive },
//       { title: "Assets", url: "/assets/list", icon: PackageOpen },
//       { title: "Asset Locations", url: "/assets/asset-locations", icon: MapPin },
//       { title: "Asset Movements", url: "/assets/movements", icon: Box },
//     ],
//   },
//   {
//     title: "Setup",
//     icon: Settings,
//     url: "/setup",
//     items: [
//       { title: "Regions", url: "/setup/regions", icon: Globe },
//       { title: "Branches", url: "/setup/branches", icon: Building2 },
//       { title: "Departments", url: "/setup/departments", icon: Briefcase },
//       { title: "Positions", url: "/setup/positions", icon: Award },
//       { title: "Ministries", url: "/setup/ministries", icon: Church },
//       { title: "Education Levels", url: "/setup/education-levels", icon: GraduationCap },
//       { title: "Institutions", url: "/setup/institutions", icon: BookOpen },
//       { title: "Marital Status", url: "/setup/marital-status", icon: Users },
//       { title: "Housing Status", url: "/setup/housing-status", icon: Building2 },
//       { title: "Occupation Types", url: "/setup/occupation-types", icon: Briefcase },
//       { title: "Skills", url: "/setup/skills", icon: Target },
//       { title: "Leadership Roles", url: "/setup/leadership-roles", icon: UserCog },
//       { title: "Religions", url: "/setup/religions", icon: Church },
//       { title: "Denominations", url: "/setup/denominations", icon: Church },
//       { title: "Currency", url: "/setup/currency", icon: DollarSign },
//     ],
//   },
//   {
//     title: "Reports",
//     icon: FileText,
//     url: "/reports",
//   },
// ]

// export function AppSidebar() {
//   return (
//     <Sidebar>
//       <SidebarHeader>
//         <div className="flex items-center gap-2 px-2 py-4">
//           <Church className="size-6 text-primary" />
//           <div className="flex flex-col">
//             <span className="text-sm font-semibold">Church Management</span>
//             <span className="text-xs text-muted-foreground">System</span>
//           </div>
//         </div>
//       </SidebarHeader>
//       <SidebarContent>
//         <SidebarGroup>
//           <SidebarGroupLabel>Main Menu</SidebarGroupLabel>
//           <SidebarGroupContent>
//             <SidebarMenu>
//               {menuItems.map((item) => (
//                 <Collapsible key={item.title} asChild defaultOpen={item.title === "Dashboard"}>
//                   <SidebarMenuItem>
//                     <CollapsibleTrigger asChild>
//                       <SidebarMenuButton tooltip={item.title}>
//                         {item.icon && <item.icon />}
//                         <span>{item.title}</span>
//                         {item.items && (
//                           <Chevr onRight className="ml-auto transition-transform duration-200 group-data-[state=open]/collapsible:rotate-90" />
//                         )}
//                       </SidebarMenuButton>
//                     </CollapsibleTrigger>
//                     {item.items && (
//                       <CollapsibleContent>
//                         <SidebarMenuSub>
//                           {item.items.map((subItem) => (
//                             <SidebarMenuSubItem key={subItem.title}>
//                               <SidebarMenuSubButton asChild>
//                                 <a href={subItem.url}>
//                                   {subItem.icon && <subItem.icon className="size-4" />}
//                                   <span>{subItem.title}</span>
//                                 </a>
//                               </SidebarMenuSubButton>
//                             </SidebarMenuSubItem>
//                           ))}
//                         </SidebarMenuSub>
//                       </CollapsibleContent>
//                     )}
//                   </SidebarMenuItem>
//                 </Collapsible>
//               ))}
//             </SidebarMenu>
//           </SidebarGroupContent>
//         </SidebarGroup>
//       </SidebarContent>
//       <SidebarFooter>
//         <div className="p-4 text-xs text-muted-foreground">v1.0.0</div>
//       </SidebarFooter>
//     </Sidebar>
//   )
// }


"use client"

import Link from "next/link"
import { useState, useEffect } from "react"
import { usePathname } from "next/navigation"
import {
  LayoutDashboard,
  Users,
  DollarSign,
  Box,
  Settings,
  FileText,
  ChevronRight,
  Church,
  UserCircle,
  Building2,
  Briefcase,
  GraduationCap,
  MapPin,
  Award,
  CalendarDays,
  CreditCard,
  Wallet,
  Receipt,
  FolderTree,
  PackageOpen,
  Archive,
  Globe,
  Layers,
  UserCog,
  Target,
  BookOpen,
} from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarHeader,
  SidebarFooter,
} from "@/components/ui/sidebar"

import { Collapsible, CollapsibleContent, CollapsibleTrigger } from "@/components/ui/collapsible"

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    url: "/dashboard",
    items: [
      { title: "Membership", url: "/dashboard/membership", icon: Users },
      { title: "Finance", url: "/dashboard/finance", icon: DollarSign },
      { title: "Assets", url: "/dashboard/assets", icon: Box },
    ],
  },
  {
    title: "Membership",
    icon: Users,
    url: "/membership",
    items: [
      { title: "Members", url: "/membership/members", icon: UserCircle },
      { title: "Branch Assignment", url: "/membership/member-branch", icon: Building2 },
      { title: "Church Positions", url: "/membership/church-positions", icon: Award },
      { title: "Department Leadership", url: "/membership/department-leadership", icon: Target },
      { title: "Ministry Assignment", url: "/membership/ministry", icon: Church },
      { title: "Education", url: "/membership/education", icon: GraduationCap },
      { title: "Occupation", url: "/membership/occupation", icon: Briefcase },
    ],
  },
  {
    title: "Finance",
    icon: DollarSign,
    url: "/finance",
    items: [
      { title: "Financial Years", url: "/finance/years", icon: CalendarDays },
      { title: "Payment Methods", url: "/finance/payment-methods", icon: CreditCard },
      { title: "Accounts", url: "/finance/accounts", icon: Wallet },
      { title: "Account Balances", url: "/finance/balances", icon: DollarSign },
      { title: "Journal Entries", url: "/finance/journals", icon: BookOpen },
      { title: "Receipts", url: "/finance/receipts", icon: Receipt },
      { title: "Donors", url: "/finance/donors", icon: Users },
      { title: "Projects", url: "/finance/projects", icon: FolderTree },
      { title: "Pledges", url: "/finance/pledges", icon: FileText },
    ],
  },
  {
    title: "Assets",
    icon: Box,
    url: "/assets",
    items: [
      { title: "Locations", url: "/assets/locations", icon: MapPin },
      { title: "Asset Categories", url: "/assets/categories", icon: Layers },
      { title: "Asset Subcategories", url: "/assets/subcategories", icon: FolderTree },
      { title: "Asset Index", url: "/assets/index", icon: Archive },
      { title: "Assets", url: "/assets/list", icon: PackageOpen },
      { title: "Asset Locations", url: "/assets/asset-locations", icon: MapPin },
      { title: "Asset Movements", url: "/assets/movements", icon: Box },
    ],
  },
  {
    title: "Setup",
    icon: Settings,
    url: "/setup",
    items: [
      { title: "Regions", url: "/setup/regions", icon: Globe },
      { title: "Branches", url: "/setup/branches", icon: Building2 },
      { title: "Departments", url: "/setup/departments", icon: Briefcase },
      { title: "Positions", url: "/setup/positions", icon: Award },
      { title: "Ministries", url: "/setup/ministries", icon: Church },
      { title: "Education Levels", url: "/setup/education-levels", icon: GraduationCap },
      { title: "Institutions", url: "/setup/institutions", icon: BookOpen },
      { title: "Marital Status", url: "/setup/marital-status", icon: Users },
      { title: "Housing Status", url: "/setup/housing-status", icon: Building2 },
      { title: "Occupation Types", url: "/setup/occupation-types", icon: Briefcase },
      { title: "Skills", url: "/setup/skills", icon: Target },
      { title: "Leadership Roles", url: "/setup/leadership-roles", icon: UserCog },
      { title: "Religions", url: "/setup/religions", icon: Church },
      { title: "Denominations", url: "/setup/denominations", icon: Church },
      { title: "Currency", url: "/setup/currency", icon: DollarSign },
    ],
  },
  {
    title: "Reports",
    icon: FileText,
    url: "/reports",
  },
]

export function AppSidebar() {
  const pathname = usePathname()
  const [openMenu, setOpenMenu] = useState<string | null>(null)

  // Auto-open active section
  useEffect(() => {
    for (const item of menuItems) {
      if (item.url === pathname) setOpenMenu(item.title)
      if (item.items?.some((s) => s.url === pathname)) setOpenMenu(item.title)
    }
  }, [pathname])

  return (
    <Sidebar>
      <SidebarHeader>
        <div className="flex items-center gap-2 px-2 py-4">
          <Church className="size-6 text-primary" />
          <div className="flex flex-col">
            <span className="text-sm font-semibold">Church Management</span>
            <span className="text-xs text-muted-foreground">System</span>
          </div>
        </div>
      </SidebarHeader>

      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Main Menu</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {menuItems.map((item) => {
                const isActive = pathname === item.url
                const isOpen = openMenu === item.title

                return (
                  <Collapsible
                    key={item.title}
                    open={isOpen}
                    onOpenChange={() => setOpenMenu(isOpen ? null : item.title)}
                    asChild
                  >
                    <SidebarMenuItem>
                      <CollapsibleTrigger asChild>
                        <SidebarMenuButton
                          tooltip={item.title}
                          isActive={isActive}
                          className={
                            isActive
                              ? "bg-gray-200 dark:bg-gray-800 font-semibold text-foreground"
                              : "hover:bg-gray-100 dark:hover:bg-gray-900"
                          }
                        >
                          <item.icon />
                          <span>{item.title}</span>

                          {item.items && (
                            <ChevronRight
                              className={`ml-auto transition-transform duration-200 ${
                                isOpen ? "rotate-90" : ""
                              }`}
                            />
                          )}
                        </SidebarMenuButton>
                      </CollapsibleTrigger>

                      {item.items && (
                        <CollapsibleContent>
                          <SidebarMenuSub>
                            {item.items.map((subItem) => {
                              const isSubActive = pathname === subItem.url

                              return (
                                <SidebarMenuSubItem key={subItem.title}>
                                  <SidebarMenuSubButton
                                    asChild
                                    isActive={isSubActive}
                                    className={
                                      isSubActive
                                        ? "bg-gray-300 dark:bg-gray-700 font-semibold text-foreground"
                                        : "hover:bg-gray-200 dark:hover:bg-gray-800"
                                    }
                                  >
                                    <Link href={subItem.url} className="flex items-center gap-2">
                                      <subItem.icon className="size-4" />
                                      <span>{subItem.title}</span>
                                    </Link>
                                  </SidebarMenuSubButton>
                                </SidebarMenuSubItem>
                              )
                            })}
                          </SidebarMenuSub>
                        </CollapsibleContent>
                      )}

                      {/* Top-level menu click if no children */}
                      {!item.items && (
                        <Link href={item.url} className="absolute inset-0" />
                      )}
                    </SidebarMenuItem>
                  </Collapsible>
                )
              })}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>

      <SidebarFooter>
        <div className="p-4 text-xs text-muted-foreground">v1.0.0</div>
      </SidebarFooter>
    </Sidebar>
  )
}

