<script lang="ts">
	import CameraIcon from '$lib/icons/CameraIcon.svelte';
	import SearchIcon from '$lib/icons/SearchIcon.svelte';
	import UploadIcon from '$lib/icons/UploadIcon.svelte';
	import type { Commander } from '$lib/interfaces/Commander';
	import commanderData from '$lib/static/commanders.json';
	import { user } from '$lib/stores/user';

	let fileinput;
	let special_num: string = '';
	let commanders: Array<Commander> = commanderData;

	$: special_num_value = +special_num ? +special_num : 0;

	const onFileSelected = (e) => {
		let image = e.target.files[0];
		let reader = new FileReader();
		reader.readAsDataURL(image);
		reader.onload = (e) => {
			$user.image_uri = e.target.result;
		};
	};

	const onNameSelected = (uri: String) => {
		$user.image_uri = uri;
	};

	let searchterm: string = '';
	$: valid_commanders = searchterm
		? commanders
				.filter((c) => c.name.toLowerCase().includes(searchterm.toLocaleLowerCase()))
				.slice(0, 20)
		: [];
</script>

<div class="card card-compact bg-base-100 shadow-xl indicator">
	<span
		class="indicator-item indicator-top indicator-center items-center justify-center inline-flex z-20"
	>
		<div class="dropdown dropdown-bottom">
			<label tabindex="0" class="btn btn-circle m-1">
				<CameraIcon />
			</label>
			<ul
				tabindex="0"
				class="dropdown-content menu flex-nowrap vertical p-2 shadow bg-base-100 rounded-box w-52 overflow-auto max-h-96"
			>
				<label for="actual-btn">
					<div class="flex py-2">
						<UploadIcon />
						<span class="pl-3"> upload </span>
					</div>
				</label>
				<input
					type="file"
					accept=".jpg, .jpeg, .png"
					on:change={(e) => onFileSelected(e)}
					bind:this={fileinput}
					id="actual-btn"
					hidden
				/>
				<div class="flex items-center justify-center">
					<SearchIcon />
					<input
						id="search-input"
						type="text"
						placeholder="search"
						class="input w-full max-w-xs"
						bind:value={searchterm}
					/>
				</div>
				{#each valid_commanders as vc}
					<button
						class="btn btn-ghost"
						on:click={() => {
							onNameSelected(vc.image_uri);
							searchterm = '';
						}}
					>
						{vc.name}
					</button>
				{/each}
			</ul>
		</div>
	</span>
	<figure class="indicator">
		<div
			class="indicator-item indicator-middle indicator-center text-white text-8xl font-bold items-center justify-center inline-flex"
		>
			{$user.life_total}
		</div>
		<div>
			<img
				src={$user.image_uri ?? 'https://placeimg.com/400/225/arch'}
				class="h-64 w-96 object-cover object-center"
				alt=""
			/>
		</div>
	</figure>
	<!-- <span class="z-40 text-white text-8xl font-bold absolute top-[50%]">40</span> -->
	<div class="card-body">
		<div class="btn-group w-full object-fill">
			<button
				class="btn btn-error w-1/2 text-2xl font-bold"
				on:click={() => ($user.life_total -= 1)}>-</button
			>
			<button
				class="btn btn-success w-1/2 text-2xl font-bold"
				on:click={() => ($user.life_total += 1)}>+</button
			>
		</div>
		<div class="btn-group w-full object-fill">
			<button
				class="btn btn-error w-1/2 text-2xl font-bold"
				on:click={() => ($user.life_total -= 5)}>-5</button
			>
			<button
				class="btn btn-success w-1/2 text-2xl font-bold"
				on:click={() => ($user.life_total += 5)}>+5</button
			>
		</div>
		<div class="input-group w-full object-fill">
			<button
				class="btn btn-error w-1/3 text-2xl font-bold"
				on:click={() => ($user.life_total -= special_num_value)}>-</button
			>
			<input
				class="input w-1/3 text-center"
				on:focus={() => special_num = ''}
				type="text"
				inputmode="numeric"
				pattern="[0-9]*"
				bind:value={special_num}
			/>
			<button
				class="btn btn-success w-1/3 text-2xl font-bold"
				on:click={() => ($user.life_total += special_num_value)}>+</button
			>
		</div>
		<div class="w-full object-fill">
			<button class="btn text-2xl font-bold w-full" on:click={() => $user.life_total = 40}>
				reset
			</button>
		</div>
	</div>
</div>
