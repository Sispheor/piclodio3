import { Piclodio3Page } from './app.po';

describe('piclodio3 App', function() {
  let page: Piclodio3Page;

  beforeEach(() => {
    page = new Piclodio3Page();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
