import { browser } from "$app/environment";
import { writable } from 'svelte/store'
import type { User } from '$lib/interfaces/User'

const defaultUser: User = {life_total: 40, image_uri: "null"}
const initialUser: User = !browser ? defaultUser : sessionStorage.getItem('user') ? JSON.parse(sessionStorage.getItem('user')) : defaultUser

export const user = writable<User>(initialUser)

if (browser){
    user.subscribe(
        (value) => {
            sessionStorage.user = JSON.stringify(value);
        }
    )
}
