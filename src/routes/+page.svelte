<script>
    import Navbar from '$lib/components/Navbar.svelte';
	import Maincard from '$lib/components/Maincard.svelte';
	import BottomNav from '$lib/components/BottomNav.svelte';
</script>

<Navbar />
<div class="flex w-screen">
	<div class="mx-auto text-center content-center items-center">
			<Maincard />
	</div>
</div>
<BottomNav />