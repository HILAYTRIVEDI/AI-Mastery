"use client"

import
{
    Sheet,
    SheetContent,
    SheetDescription,
    SheetHeader,
    SheetTitle,
    SheetTrigger,
} from "@/components/ui/sheet"
import Link from "next/link"
import Image from "next/image"
import { SignedIn, SignedOut, UserButton } from "@clerk/nextjs"
import { navLinks } from "@/constants/index"
import { usePathname } from "next/navigation"
import { Button } from "@/components/ui/button"

const MobileNav = () =>
{
    const pathName = usePathname()
    return (
        <header className="header">
            <Link href='/' className="flex items-center gap-2 md:py-2">
                <Image
                    src='/assets/images/logo-text.svg'
                    alt='Logo'
                    width={180}
                    height={28}
                />
            </Link>
            <nav className="flex gap-2">
                <SignedIn>
                    <UserButton />
                    <Sheet>
                        <SheetTrigger>
                            <Image
                                src='/assets/icons/menu.svg'
                                alt='Menu'
                                width={32}
                                height={32}
                                className="cursor-pointer"
                            />
                        </SheetTrigger>
                        <SheetContent className="sheet-content sm:w-64">
                            <>
                                <Image
                                    src='/assets/images/logo-text.svg'
                                    alt='Logo'
                                    width={152}
                                    height={23}
                                />
                                <ul className="header-nav_elements">
                                    {
                                        navLinks.map((link, index) =>
                                        {
                                            const isActive = link.route === pathName;

                                            return (
                                                <li
                                                    key={link.route}
                                                    className={
                                                        `${isActive && 'gradient-text'} p-18 flex whitespace-nowrap text-dark-700`
                                                    }>
                                                    <Link href={link.route} className='sidebar-link cursor-pointer'>
                                                        <Image
                                                            src={link.icon}
                                                            alt='Logo'
                                                            width={24}
                                                            height={24}
                                                        />
                                                        {link.label}
                                                    </Link>
                                                </li>
                                            )
                                        })
                                    }
                                    <li className='flex-center cursor-pointer gap-2 p-4'>
                                        <UserButton showName />
                                    </li>
                                </ul>
                            </>
                        </SheetContent>
                    </Sheet>
                </SignedIn>
                <SignedOut>
                    <Button variant='default' size='default' asChild className='bg-purple-gradient bg-purple'>
                        <Link href='/sign-in'>Sign In</Link>
                    </Button>
                </SignedOut>
            </nav>
        </header>
    )
}

export default MobileNav