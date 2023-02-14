<script>
	import Github from '$lib/icons/Github.svelte';
	import MenuIcon from '$lib/icons/MenuIcon.svelte';
	import Themetoggle from './Themetoggle.svelte';
</script>

<div class="navbar bg-base-100 mb-2">
	<div class="navbar-start">
		<div class="dropdown hidden md:block">
			<label tabindex="0" class="btn btn-ghost btn-circle">
				<MenuIcon />
			</label>
			<ul
				tabindex="0"
				class="menu menu-compact dropdown-content mt-3 p-2 shadow bg-base-100 rounded-box w-52"
			>
				<li><a>Home</a></li>
				<li><a>Games</a></li>
				<li><a>User Settings</a></li>
			</ul>
		</div>
	</div>
	<div class="navbar-center">
		<a class="btn btn-ghost normal-case text-xl">commander</a>
	</div>
	<div class="navbar-end">
		<a href="/">
			<Github />
		</a>
		<Themetoggle />
	</div>
</div>
