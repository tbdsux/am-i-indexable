<script>
  let url = "";
  let finalQ = "";
  let formBtnText = "Find";
  let queryDone = false;

  // init search-results
  let qResults = [];

  let searchEngines = ["Google", "Bing", "DuckDuckGo", "Ask"];

  function handleSearch() {
    qResults = []; // reset results

    formBtnText = "Getting...";
    searchEngines.map((se) => {
      fetch(`/api/search/${se.toLowerCase()}?q=${url}`, {
        method: "GET",
      })
        .then((dat) => dat.text())
        .then((res) => {
          qResults = [
            ...qResults,
            {
              site: se,
              result: res === "true",
            },
          ];
        });
    });
  }
  // reactive if
  $: if (qResults.length > 0) {
    queryDone = true;

    formBtnText = "Find";
  }
</script>

<main>
  <div class="py-24 w-4/5 mx-auto text-center relative">
    <div class="absolute top-4 right-4">
      <a
        href="https:/github.com/TheBoringDude"
        title="Goto Github"
        rel="noreferrer"
        class="text-gray-500 hover:underline tracking-wide">Github</a
      >
    </div>

    <div>
      <h1 class="font-black tracking-wide text-6xl text-gray-600">
        Am I Indexable?
      </h1>
      <p class="mt-4 text-xl tracking-wide">
        Search your website if indexable by the search engines....
      </p>
    </div>

    <!-- form -->
    <div class="w-2/3 mx-auto py-8">
      <input
        type="text"
        bind:value={url}
        class="border rounded-full text-center py-3 px-6 w-full tracking-wide text-xl font-light"
        placeholder="Enter a website url"
      />
      <button
        on:click={handleSearch}
        class="py-3 px-12 rounded-full bg-gray-500 hover:bg-gray-600 mt-2 text-xl uppercase font-bold text-white"
        >{formBtnText}</button
      >
    </div>

    <hr />

    {#if queryDone}
      <!-- search results -->
      <div class="w-3/4 mx-auto py-8">
        <h4 class="text-left mb-4 text-lg text-gray-500">
          Website: <span class="font-bold tracking-wide text-gray-600"
            >{url}</span
          >
        </h4>

        <ul>
          {#each qResults as qr}
            <li
              class="flex items-center justify-between my-2 py-3 px-6 rounded-full text-xl border {qr.result
                ? 'border-green-500'
                : 'border-yellow-500'}"
            >
              <h3 class="font-bold tracking-wide text-gray-600">
                {qr.site}
              </h3>

              <span class="font-bold tracking-wider uppercase text-gray-700"
                >{qr.result ? "Searchable" : "No results"}</span
              >
            </li>
          {/each}
        </ul>
      </div>
    {/if}
  </div>
</main>
